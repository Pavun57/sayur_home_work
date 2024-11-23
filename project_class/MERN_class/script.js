document.addEventListener("DOMContentLoaded", () => {
    const taskInput = document.getElementById("taskInput");
    const addTaskBtn = document.getElementById("addTaskBtn");
    const taskList = document.getElementById("taskList");
  
    // Load tasks from localStorage
    const loadTasks = () => {
      const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
      taskList.innerHTML = ""; // Clear the list
      tasks.forEach((task, index) => createTaskElement(task, index));
    };
  
    // Save tasks to localStorage
    const saveTasks = () => {
      const tasks = [];
      document.querySelectorAll("#taskList li").forEach((li) => {
        tasks.push(li.firstChild.textContent);
      });
      localStorage.setItem("tasks", JSON.stringify(tasks));
    };
  
    // Create a task element
    const createTaskElement = (task, index) => {
      const li = document.createElement("li");
      li.textContent = task;
  
      // Add delete button
      const deleteBtn = document.createElement("button");
      deleteBtn.textContent = "Delete";
      deleteBtn.addEventListener("click", () => {
        li.remove();
        saveTasks();
      });
  
      li.appendChild(deleteBtn);
      taskList.appendChild(li);
    };
  
    // Add task
    addTaskBtn.addEventListener("click", () => {
      const task = taskInput.value.trim();
      if (task) {
        createTaskElement(task);
        saveTasks();
        taskInput.value = "";
      }
    });
  
    // Initialize
    loadTasks();
  });
  