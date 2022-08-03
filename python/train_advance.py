from cortex import Cortex

class TrainAdvance():
	def __init__(self):
		self.c = Cortex(user, debug_mode=True)
		self.c.do_prepare_steps()

	def get_active_action(self, profile_name):
		self.c.get_mental_command_active_action(profile_name)

	def get_command_brain_map(self, profile_name):
		self.c.get_mental_command_brain_map(profile_name)

	def get_training_threshold(self):
		self.c.get_mental_command_training_threshold(profile_name)

# ---------------------------------------------------

user = {
	"license" : "",
	"client_id" : 'NxyEzxFWW84LtcvZ1sFsD7XOVtTskofcWP0jRpVq',
	"client_secret" : 'N7Njh53gWrdlbfwqbSdNKvxfTh2jjKvkPrQ57TtXcGKeMW7f6UQ9nBbNrXNj02UaB2pdgEtbYTrjcKzTQ53rtC5nLdVUwmWcPlmHtpVXUwL1o5FsJks3tv4LPh77PTs4',
	"debit" : 100
}

t = TrainAdvance()

profile_name = 'your trained profile name'

t.get_active_action(profile_name)
t.get_command_brain_map(profile_name)
t.get_training_threshold()

# ---------------------------------------------------