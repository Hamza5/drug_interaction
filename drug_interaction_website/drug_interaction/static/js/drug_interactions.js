function addField(clickEvent) {
    const field = document.createElement("input");
    field.setAttribute("type", "text");
    field.setAttribute("name", "drugs");
    field.setAttribute("placeholder", "Drug name");
    const removeButton = document.createElement("button");
    removeButton.setAttribute("type", "button");
    removeButton.setAttribute("class", "remove-drug");
    removeButton.textContent = "-";
    removeButton.addEventListener("click", removeField);
    const container = document.createElement('div');
    container.appendChild(field);
    container.appendChild(removeButton);
    clickEvent.target.parentNode.insertBefore(container, clickEvent.target);
}

function removeField(clickEvent) {
    const container = clickEvent.target.parentNode;
    container.parentNode.removeChild(container);
}

document.addEventListener("DOMContentLoaded", () => {
    const addButton = document.getElementById("add-drug");
    addButton.addEventListener("click", addField);
    const removeButtons = document.getElementsByClassName("remove-drug");
    for (const button of removeButtons) {
        button.addEventListener("click", removeField);
    }
});