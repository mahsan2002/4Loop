// Wait for the entire DOM to be loaded before executing the script
document.addEventListener('DOMContentLoaded', () => {
    // Get references to key elements in the DOM
    const tree = document.getElementById('tree'); // The tree container
    const trunk = document.querySelector('#tree .trunk'); // The trunk element of the tree
    const leaves = document.querySelector('#tree .leaves'); // The leaves element of the tree
    const pointsDisplay = document.getElementById('pointsDisplay'); // Display for total points
    const walkingPointsDisplay = document.getElementById('walkingPoints'); // Display for walking points
    const foodPointsDisplay = document.getElementById('foodPoints'); // Display for food points
    const recyclingPointsDisplay = document.getElementById('recyclingPoints'); // Display for recycling points
    const plasticPointsDisplay = document.getElementById('plasticPoints'); // Display for plastic points

    // Initialize state variables
    let trunkHeight = 150; // Initial height of the trunk
    let leavesSize = 200; // Initial size (width and height) of the leaves
    let totalPoints = 0; // Total points accumulated
    let walkingPoints = 0; // Points from walking
    let foodPoints = 0; // Points from food
    let recyclingPoints = 0; // Points from recycling
    let plasticPoints = 0; // Points from plastic reduction

//    // Initialize Bootstrap popovers for buttons with data-toggle="popover"
//    $('[data-toggle="popover"]').popover({
//        trigger: 'hover', // Show popover on hover
//        placement: 'top' // Place popover above the button
//    });

    const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
    const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

    // Function to grow the tree based on the activity and points
    function growTree(points, activity) {
        // Update tree dimensions and points based on the activity
        trunkHeight += points; // Increase trunk height by the number of points
        leavesSize += points * 0.5; // Increase leaves size by half the number of points
        totalPoints += points; // Update total points

        // Update activity-specific points and display
        if (activity === 'walking') {
            walkingPoints += points;
            walkingPointsDisplay.textContent = walkingPoints; // Update walking points display
        } else if (activity === 'food') {
            foodPoints += points;
            foodPointsDisplay.textContent = foodPoints; // Update food points display
        } else if (activity === 'recycling') {
            recyclingPoints += points;
            recyclingPointsDisplay.textContent = recyclingPoints; // Update recycling points display
        } else if (activity === 'plastic') {
            plasticPoints += points;
            plasticPointsDisplay.textContent = plasticPoints; // Update plastic points display
        }

        // Update the tree's trunk height and leaves size
        trunk.style.height = `${trunkHeight}px`; // Set the new height of the trunk
        leaves.style.width = `${leavesSize}px`; // Set the new width of the leaves
        leaves.style.height = `${leavesSize}px`; // Set the new height of the leaves
        tree.style.height = `${trunkHeight + leavesSize / 2}px`; // Adjust the tree container height
        pointsDisplay.textContent = `Points: ${totalPoints}`; // Update the total points display
    }

    // Add event listeners to all buttons with class "grow-button"
    document.querySelectorAll('.grow-button').forEach(button => {
        button.addEventListener('click', (event) => {
            // Retrieve points and activity type from button attributes
            const points = parseInt(event.target.getAttribute('data-points'));
            // Get activity type from the button's data-activity attribute
            const activity = event.target.getAttribute('data-activity');
            // Call the function to grow the tree based on the clicked button
            growTree(points, activity);
        });
    });
});
