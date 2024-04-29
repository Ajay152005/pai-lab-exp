class ForwardChaining:
    def __init__(self, knowledge_base, goal):
        self.knowledge_base = knowledge_base
        self.agenda = [goal]
        self.facts = set()
        self.goal = goal
    def apply_rule(self, rule):
        if "=>" in rule:
            antecendent, consequent = rule.split("=>")
            antecendent_facts = antecendent.strip().split(" and ")
            if all(fact in self.facts for fact in antecendent_facts):
                new_fact = consequent.strip()
                self.facts.add(new_fact)
                print(f"Applied rule: {rule}. Added new fact: {new_fact}")
                return True
        return False
    def ForwardChaining(self):
        while self.agenda:
            current_fact = self.agenda.pop(0)
            if current_fact in self.facts:
                continue
