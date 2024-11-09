function toggleTaskStatus(taskId) {
    fetch(`/tasks/${taskId}/toggle/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}'
      },
      body: JSON.stringify({ id: taskId })
    })
    .then(response => response.json())
    .then(data => {
      const icon = document.getElementById(`taskCompleted${taskId}`);
      if (data.completed) {
        icon.classList.remove('bi-square');
        icon.classList.add('bi-check-square');
      } else {
        icon.classList.remove('bi-check-square');
        icon.classList.add('bi-square');
      }
    });
  }