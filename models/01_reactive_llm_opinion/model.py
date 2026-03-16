import mesa
from mesa.experimental.dev import Signal

class OpinionAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        # 4.0 Reactive Pattern: Agents connect to signals
        self.model.info_signal.connect(self.process_opinion)

    def process_opinion(self, msg):
        # In a full model, this triggers an LLM call
        print(f"Agent {self.unique_id} reacting to info: {msg}")

class ReactiveLLMModel(mesa.Model):
    def __init__(self):
        super().__init__()
        self.info_signal = Signal()
        for i in range(5):
            OpinionAgent(self)
            
    def step(self):
        if self.steps % 5 == 0:
            self.info_signal.emit("New architectural standard in Mesa 4.0!")