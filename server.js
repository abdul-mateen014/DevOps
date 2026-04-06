const path = require('path');
const fs = require('fs');
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;
const dbFile = process.env.DB_FILE || path.join(__dirname, 'notes.db');

if (!fs.existsSync(path.dirname(dbFile))) {
  fs.mkdirSync(path.dirname(dbFile), { recursive: true });
}

const db = new sqlite3.Database(dbFile);

db.serialize(() => {
  db.run(`
    CREATE TABLE IF NOT EXISTS notes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
  `);
});

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.get('/api/health', (_req, res) => {
  res.json({ status: 'ok' });
});

app.get('/api/notes', (_req, res) => {
  db.all('SELECT * FROM notes ORDER BY id DESC', [], (error, rows) => {
    if (error) {
      return res.status(500).json({ message: 'Failed to fetch notes' });
    }

    res.json(rows);
  });
});

app.post('/api/notes', (req, res) => {
  const title = (req.body.title || '').trim();

  if (!title) {
    return res.status(400).json({ message: 'Title is required' });
  }

  db.run('INSERT INTO notes (title) VALUES (?)', [title], function (error) {
    if (error) {
      return res.status(500).json({ message: 'Failed to create note' });
    }

    res.status(201).json({
      id: this.lastID,
      title
    });
  });
});

app.delete('/api/notes/:id', (req, res) => {
  db.run('DELETE FROM notes WHERE id = ?', [req.params.id], function (error) {
    if (error) {
      return res.status(500).json({ message: 'Failed to delete note' });
    }

    if (this.changes === 0) {
      return res.status(404).json({ message: 'Note not found' });
    }

    res.json({ message: 'Deleted successfully' });
  });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});