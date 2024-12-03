const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');

// Define a schema for items
const itemSchema = new mongoose.Schema({
  id: String,
  name: String,
  description: String,
  price: Number
});

// Create a model for items
const Item = mongoose.model('Item', itemSchema);

// CREATE - Add new item
router.post('/items', async (req, res) => {
  try {
    const newItem = new Item({ id: Date.now().toString(), ...req.body });
    await newItem.save();
    res.status(201).json(newItem);
  } catch (error) {
    res.status(500).json({ message: 'Error creating item', error });
  }
});

// READ - Get all items
router.get('/items', async (req, res) => {
  try {
    const items = await Item.find();
    res.json(items);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching items', error });
  }
});

// READ - Get single item
router.get('/items/:id', async (req, res) => {
  try {
    const item = await Item.findOne({ id: req.params.id });
    if (item) {
      res.json(item);
    } else {
      res.status(404).json({ message: 'Item not found' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Error fetching item', error });
  }
});

// UPDATE - Update an item
router.put('/items/:id', async (req, res) => {
  try {
    const item = await Item.findOneAndUpdate({ id: req.params.id }, req.body, { new: true });
    if (item) {
      res.json(item);
    } else {
      res.status(404).json({ message: 'Item not found' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Error updating item', error });
  }
});

// DELETE - Delete an item
router.delete('/items/:id', async (req, res) => {
  try {
    const item = await Item.findOneAndDelete({ id: req.params.id });
    if (item) {
      res.json({ message: 'Item deleted successfully', item });
    } else {
      res.status(404).json({ message: 'Item not found' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Error deleting item', error });
  }
});

module.exports = router;
