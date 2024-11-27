document.addEventListener("DOMContentLoaded", function(event) {
    // Get all elements with the class 'hidden-heading-field'
    const elements = document.querySelectorAll(".hidden-heading-field");

    elements.forEach(element => {
        // Get the data-heading attribute and trim whitespace
        const headingText = element.getAttribute("data-heading").trim();

        // Create the new element to prepend
        let newElement;
        if (headingText === "") {
            // If data-heading is empty or whitespace, create a horizontal line
            newElement = document.createElement("hr");
        } else {
            // Otherwise, create an h4 header with the headingText
            newElement = document.createElement("h4");
            newElement.textContent = headingText;
        }

        // Prepend the new element before the current element
        element.parentNode.insertBefore(newElement, element);
    });
});
