var $ = jQuery;
// var container;
// var group_clone;
// var row_clone;
// var header_clone;
var exchange_interval;
$(window).load(function  () {
// $(document).ready(function($) {
  container = $('.vfx_exchange_rate');
  group_clone = container.find(".group").remove().clone();
  row_clone = group_clone.find(".row").clone();
  header_clone = container.find(".header").remove().clone();
  update_data();
  exchange_interval = setInterval(update_data, refresh_rate);
  setTimeout(function(){
    clearTimeout(exchange_interval);
  }, 10*60*1000);
});

function update_data(skip_animation){
  skip_animation = typeof skip_animation !== 'underfined' ? skip_animation : false;
  var visible_symbols = symbols;
  var data = {
    'action': 'vfx_get_exchange_rate',
    'symbols': visible_symbols,
    'token': accessToken
  };
  $.ajax({
    url:"https://feed.vantagefx.com/exchange",
    data:data,
    dataType:"jsonp" ,
    error:function(xhr, ajaxOption, throwError){
        clearTimeout(exchange_interval);
    },
    success:function(response) {
      var json = response;

      if('error' in json){
        clearTimeout(exchange_interval);
        return;
      }

      $.each(json, function(key, symbols){
        if($.inArray(key, groups) < 0){
          return;
        }
        var current_group;
        var group_first = true;
        if(container.find("." + key).length >= 1){
          current_group = container.find("." + key);
          group_first = false;
        }else{
          current_group = group_clone.clone().empty();
          var header = header_clone.clone();
          $(header.find("h1")[0]).text(key);
          current_group.append(header);
        }
        if(skip_animation){
          $.each(symbols, function(index, value){
            if($.inArray(value['symbol'], visible_symbols) < 0){
              return;
            }
            var current_row;
            var first = true;
            if(current_group.find("." + value['symbol']).length >= 1){
              first = false;
              var current_row = current_group.find("." + value['symbol']);
            }else{
              var current_row = row_clone.clone();
            }
            apply_change(current_row.find('.symbol'), value['symbol'], false);
            apply_change(current_row.find('.bid'), value['bid'], false);
            apply_change(current_row.find('.ask'), value['ask'], false)
            apply_change(current_row.find('.spread'),(parseFloat(value['spread'])/10).toFixed(1), false);
            if(first){
              current_row.addClass(value["symbol"])
              current_group.append(current_row);
            }
          })
        }else{
            $.each(symbols, function(index, value){
              if($.inArray(value['symbol'], visible_symbols) < 0){
                return;
              }
              var current_row;
              var first = true;
              if(current_group.find("." + value['symbol']).length >= 1){
                first = false;
                var current_row = current_group.find("." + value['symbol']);
              }else{
                var current_row = row_clone.clone();
              }
              setTimeout(function(){
                apply_change(current_row.find('.symbol'), value['symbol'], false)
                apply_change(current_row.find('.bid'), value['bid'], true)
                apply_change(current_row.find('.ask'), value['ask'], true)
                apply_change(current_row.find('.spread'), (parseFloat(value['spread'])/10).toFixed(1), true);
              }, Math.random() * refresh_rate);
              if(first){
                current_row.addClass(value["symbol"])
                current_group.append(current_row);
              }
            })
        }
        if(group_first){
          current_group.addClass(key);
          container.append(current_group);
        }
      });
    }});
}
function apply_change(element, data, add_classes){
  add_classes = typeof add_classes !== 'underfined' ? add_classes : false;
  if(data != element.text()){
    if(add_classes){
      element.addClass("changed");
      element.parent().addClass("changed");
      if(data < element.text() ){
        //decreased
        element.addClass("decreased");
        element.parent().addClass("decreased");

      }else{
        element.addClass("increased");
        element.parent().addClass("increased");
      }
    }
    element.text(data);
    setTimeout(function(){element.parent().removeClass("changed decreased increased")}, decoration_timeout);
    setTimeout(function(){element.removeClass("changed decreased increased")}, decoration_timeout);
  }
}
update_data(true);
