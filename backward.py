class BackwardChaining:
    def __init__(self, facts, rules):
        self.facts = facts
        self.rules = rules
    def backward_chaining(self, goal):
        print(f'Attemping to achieve goal: {goal}')
        count = 0
        matched = []

        if goal in self.facts:
            print(f"Goal '{goal}' is a known fact, Goal achieved!")
            return True
        if goal in self.rules:
            subgoals = self.rules[goal]

            for subgoal in subgoals:
                if self.backward_chaining(subgoal):
                    count += 1
                    matched.append(subgoal)
                    
            if count > 0:
                print(f'true, \nfact alligned : , {matched}')
                return True
        print(f"Goal '{goal}' cannot be achieved. Goal not satisfied.")
        return False

known_facts = ['fact_A', 'fact_B','fact_C']
rule_base = {'goal_A': ['fact_A', 'fact_B'], 'goal_B': ['fact_C', 'goal_A'],
             'unknown_A': ['uh','fact_A','unknown1','uhhh']}

backward_chaining_system = BackwardChaining(known_facts, rule_base)

result = backward_chaining_system.backward_chaining('goal_A')

print(f"Overall result: {result}")