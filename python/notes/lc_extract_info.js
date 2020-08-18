var rows = $(".reactable-data tr");

var data = [];
rows.toArray().forEach(function (row) {
  var s = row.cells[6].firstChild.firstChild.getAttribute("style");
  var el = {
    ID: row.cells[1].innerText,
    TITLE: row.cells[2].firstChild.getAttribute("data-original-title"),
    PASS: row.cells[4].innerText,
    DIFFICULTY: row.cells[5].getElementsByTagName("span")[0].innerText,
    FREQUENCY: Number(s.substring(7, s.length - 3)).toFixed(2)
  };
  data.push(el);
  // console.info(el);
});
console.warn(JSON.stringify(data));