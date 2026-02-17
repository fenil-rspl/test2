const User = require('../models/User');

exports.getUser = async (id) => {
	const user = await User.findById(id);
	if (!user) {
		throw new Error('User not found');
	}
	return user;
};