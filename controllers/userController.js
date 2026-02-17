const userService = require('../services/userService');

exports.getUser = async (req, res) => {
	try {
		const user = await userService.getUser(req.params.id);
		res.status(200).json(user);
	} catch (error) {
		res.status(404).json({ message: error.message });
	}
};