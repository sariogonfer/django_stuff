Element.prototype.getParentByTagName = function(tagName) {
    var parent;
	if (this === null || tagName === '') return;
	parent  = this.parentNode;
	tagName = tagName.toUpperCase();

	while (parent.tagName !== "HTML") {
		if (parent.tagName === tagName) {
			return parent;
		}
		parent = parent.parentNode;
	}

	return undefined;
};

function addRowToCompleteText(elem) {
    var table = elem.parentNode.parentNode.parentNode;
    var row_template = table.getElementsByClassName('row_template')[0];

    var cp = row_template.cloneNode(true);
    cp.removeAttribute("style");
    cp.className = cp.className.replace('row_template', '');
    table.insertBefore(cp, elem.getParentByTagName('tr'));
    initCompleteTextFields();
};

function extractResult(elem) {
    var result = "";
    var result_template = elem.getAttribute("result_template");
    var row_list = elem.querySelectorAll('tr.row:not(.row_template):not(.add-button)');
    for (var i = 0; i < row_list.length; i++) {
        var input_list = row_list[i].getElementsByTagName('input');
        var foo = result_template;
        for (var j = 0; j < input_list.length; j++){
            var biz = input_list[j],
            foo = foo.replace(biz.getAttribute('tag'), biz.value);
        }
        result += foo;
    }

    return result;
};

function updateCompleteTextInputResult (ev) {
    target = ev.target;
    table = target.getParentByTagName('table');
    result_input = table.nextElementSibling;
    result_input.value = extractResult(table);
};

function initCompleteTextFields() {
    var tables = document.getElementsByClassName('complete-text-input-table');
    for (var i = 0; i < tables.length; i++){
        var inputs = tables[i].getElementsByTagName('input');
        for (var j = 0; j < inputs.length; j ++) {
            inputs[j].onkeyup = updateCompleteTextInputResult;
        }
    }
};

document.addEventListener('DOMContentLoaded', function() {
    initCompleteTextFields();
}, false);

function run () {
    var tables = document.getElementsByClassName('complete-text-input-table');
    for (var i = 0; i < tables.length; i++) {
        console.log(extractResult(tables[i]));
    }
};