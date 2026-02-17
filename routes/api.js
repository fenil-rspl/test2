const express = require('express');
const router = express.Router();
const apiController = require('../controllers/apiController');

router.get('/health', apiController.healthCheck);

module.exports = router;