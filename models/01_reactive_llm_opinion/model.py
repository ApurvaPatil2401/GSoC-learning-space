import mesa

class OpinionAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)

    def process_opinion(self, msg):
        # This is your reactive trigger for the LLM
        print(f"Agent {self.unique_id} reacting to info: {msg}")

class ReactiveLLMModel(mesa.Model):
    def __init__(self):
        super().__init__()
        for i in range(5):
            OpinionAgent(self)

    def step(self):
        # Standard Mesa 4.0 way to trigger a specific behavior reactively
        if self.steps % 5 == 0:
            msg = "New architectural standard in Mesa 4.0!"
            self.agents.do("process_opinion", msg)
        
        self.agents.step()
