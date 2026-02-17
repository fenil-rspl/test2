const User = require('../models/User');
const jwt = require('jsonwebtoken');
const constants = require('../config/constants');

exports.login = async (email, password) => {
	const user = await User.findOne({ email });
	if (!user || user.password !== password) {
		throw new Error('Invalid credentials');
	}
	return jwt.sign({ id: user._id }, constants.JWT_SECRET, { expiresIn: constants.JWT_EXPIRATION });
};

exports.register = async (data) => {
	const user = new User(data);
	return await user.save();
};