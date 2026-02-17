const jwt = require('jsonwebtoken');
const constants = require('../config/constants');

const auth = (req, res, next) => {
	const token = req.headers['authorization'];
	if (!token) return res.status(403).send('A token is required for authentication');
	try {
		const decoded = jwt.verify(token, constants.JWT_SECRET);
		req.user = decoded;
	} catch (err) {
		return res.status(401).send('Invalid Token');
	}
	return next();
};

module.exports = auth;