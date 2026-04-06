const form = document.getElementById('note-form');
const titleInput = document.getElementById('title');
const notesList = document.getElementById('notes');
const statusEl = document.getElementById('status');

function setStatus(message) {
  statusEl.textContent = message;
}

function renderNotes(notes) {
  notesList.innerHTML = '';

  if (!notes.length) {
    notesList.innerHTML = '<li>No notes yet. Add your first one.</li>';
    return;
  }

  notes.forEach((note) => {
    const item = document.createElement('li');
    item.innerHTML = `
      <span>${note.title}</span>
      <button data-id="${note.id}">Delete</button>
    `;
    notesList.appendChild(item);
  });
}

async function loadNotes() {
  const response = await fetch('/api/notes');
  const notes = await response.json();
  renderNotes(notes);
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const title = titleInput.value.trim();

  if (!title) {
    setStatus('Please enter a note.');
    return;
  }

  const response = await fetch('/api/notes', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title })
  });

  if (!response.ok) {
    setStatus('Unable to add note.');
    return;
  }

  titleInput.value = '';
  setStatus('Note added successfully.');
  await loadNotes();
});

notesList.addEventListener('click', async (event) => {
  if (event.target.tagName !== 'BUTTON') {
    return;
  }

  const id = event.target.dataset.id;
  const response = await fetch(`/api/notes/${id}`, { method: 'DELETE' });

  if (!response.ok) {
    setStatus('Unable to delete note.');
    return;
  }

  setStatus('Note deleted.');
  await loadNotes();
});

loadNotes().catch(() => setStatus('Could not load notes.'));