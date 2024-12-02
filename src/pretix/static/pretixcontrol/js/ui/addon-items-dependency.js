document.addEventListener("DOMContentLoaded", function(event) {
    // Select all inputs with the data-addon-item-dependency-id attribute
    const dependentCheckboxes = document.querySelectorAll('input[type="checkbox"][data-addon-item-dependency-id]');

    // Loop through each checkbox and add an event listener
    dependentCheckboxes.forEach(function (checkbox) {

        const sourceId = checkbox.id;
        // Get the id of the dependent checkbox
        const dependentId = checkbox.getAttribute('data-addon-item-dependency-id');
        const dependentCheckbox = document.getElementById(dependentId);

        const sourceInfoElement = document.getElementById(`${sourceId}_addon_dependency_info`);
        const legendElement = document.getElementById(`${dependentId.replace(/_/g, '-')}-legend`);

        // Check if both elements exist
        if (sourceInfoElement && legendElement) {
            const legendText = legendElement.innerText || legendElement.textContent;
            // Set the innerText of the dependency info element
            sourceInfoElement.innerHTML = `Dieses Produkt ist nur zusammen wählbar mit: <strong>${legendText}</strong>`;
        }

        // Function to check if the dependent checkbox is checked and update the current checkbox
        function checkDependency() {
            if (dependentCheckbox && dependentCheckbox.checked) {
                // If the dependent checkbox is checked, enable the current checkbox
                checkbox.disabled = false;
            } else {
                // If the dependent checkbox is not checked, disable the current checkbox and uncheck it
                checkbox.disabled = true;
                checkbox.checked = false;
            }
        }

        // Add event listeners to both the current checkbox and the dependent checkbox
        checkbox.addEventListener('change', checkDependency);  // When the current checkbox changes
        dependentCheckbox.addEventListener('change', checkDependency);  // When the dependent checkbox changes

        // Initial check in case the page loads with a pre-checked dependent checkbox
        checkDependency();
    });
});
