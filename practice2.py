class ForwardChaining:
    def __init__(self, knowledge_base, goal):
        self.knowledge_base = knowledge_base
        self.agenda = [goal]
        self.facts = set()
        self.goal = goal

    def apply_rule(self, rule):
        if '=>' in rule:
            antecedent, consequent = rule.split("=>")
            antecedent_facts = antecedent.strip().split(" and ")
            if all(fact in self.facts for fact in antecedent_facts):
                new_fact = consequent.strip()
                self.facts.add(new_fact)
                print(f"Applied rule: {rule}. Added new fact: {new_fact}")
                return True
            return False
    def forward_chain(self):
        while self.agenda:
            current_fact = self.agenda.pop(0)
            if current_fact in self.facts:
                continue
            self.facts.add(current_fact)
            print(f"Current fact: {current_fact}")
            for rule in self.knowledge_base:
                if self.apply_rule(rule):
                    self.agenda.append(current_fact)
        if self.goal in self.facts:
            print('Goal achieved!')
            return True
        else:
            print('Goal not achieved')
            return False
if __name__ == "__main__":
    knowledge_base = [
        "Hungry",
        "No groceries at home",
        "No time to cook",
        "hungry and no groceries at home and no time to cook => eat out",
        "eat out => Check restaurant reviews",
        "check restaurant reviews"
    ]

    goal = "check restaurant reviews"

    forwardChaining = ForwardChaining(knowledge_base, goal)
    forwardChaining.forward_chain()