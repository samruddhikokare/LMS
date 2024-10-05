document.addEventListener('DOMContentLoaded', function () {
    const enrollButtons = document.querySelectorAll('.enroll-button');
    const progressButtons = document.querySelectorAll('.mark-completed');

    // Fetch courses on page load
    fetchCourses();

    // Add event listeners for enrolling in courses
    enrollButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            const courseId = e.target.dataset.courseId;
            enrollInCourse(courseId);
        });
    });

    // Add event listeners for marking courses as completed
    progressButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            const courseId = e.target.dataset.courseId;
            markCourseCompleted(courseId);
        });
    });
});

// Function to fetch courses from the backend
async function fetchCourses() {
    try {
        const response = await fetch('/api/courses/');
        const courses = await response.json();
        displayCourses(courses);
    } catch (error) {
        console.error('Error fetching courses:', error);
    }
}

// Function to display courses in the UI
function displayCourses(courses) {
    const courseContainer = document.getElementById('course-list');
    courseContainer.innerHTML = '';

    courses.forEach(course => {
        const courseElement = document.createElement('div');
        courseElement.classList.add('course');

        courseElement.innerHTML = `
            <h3>${course.title}</h3>
            <p>${course.description}</p>
            <button class="enroll-button" data-course-id="${course.id}">Enroll</button>
            <button class="mark-completed" data-course-id="${course.id}">Mark as Completed</button>
        `;

        courseContainer.appendChild(courseElement);
    });
}

// Function to enroll in a course
async function enrollInCourse(courseId) {
    try {
        const response = await fetch(`/api/enroll/${courseId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (response.ok) {
            alert('Successfully enrolled in the course!');
            fetchCourses(); // Refresh course list
        } else {
            alert('Failed to enroll in the course. Please try again.');
        }
    } catch (error) {
        console.error('Error enrolling in course:', error);
    }
}

// Function to mark a course as completed
async function markCourseCompleted(courseId) {
    try {
        const response = await fetch(`/api/complete/${courseId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (response.ok) {
            alert('Course marked as completed!');
            fetchCourses(); // Refresh course list
        } else {
            alert('Failed to mark course as completed. Please try again.');
