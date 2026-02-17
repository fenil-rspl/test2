const express = require('express');
const router = express.Router();
const apiController = require('../controllers/apiController');
const authRoutes = require('./auth');
const userRoutes = require('./users');

router.use('/auth', authRoutes);
router.use('/users', userRoutes);
router.get('/health', apiController.healthCheck);

module.exports = router;