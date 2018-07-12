var cnt = 2;
console.log(cnt);
function addField(){
  var parent = document.getElementById('choice_field');

  var x = document.createElement('INPUT');
  x.setAttribute('type','text');
  x.setAttribute('name','ip'+cnt.toString());
  document.getElementById('num').value = cnt;
  cnt++;

  parent.append(x);
}
