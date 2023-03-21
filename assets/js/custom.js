count = 1;
function addTextBox() {
    event.preventDefault()
    // Clone the text box element
    var textBox = document.getElementById("addSource");
    var newTextBox = textBox.cloneNode(true);

    var field1 = newTextBox.querySelector('input[name="text_box_"]');
    field1.setAttribute('name', 'text_box_' + count);
    count += 1;

    // Add the new text box element to the page
    var container = document.getElementById("helluh");
    container.appendChild(newTextBox);
}

var addButton = document.getElementById("add-source");
addButton.addEventListener("click", addTextBox);
