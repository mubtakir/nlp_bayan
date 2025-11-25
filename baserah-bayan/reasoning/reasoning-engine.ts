import { MotherEquation, ObjectType } from "../core/mother-equation";

export class ReasoningEngine extends MotherEquation {
  rules: Array<{premises: Record<string, any>; conclusion: Record<string, any>}>;
  
  constructor(name: string) {
    super(ObjectType.ABSTRACT, name);
    this.rules = [];
  }
  
  addRule(premises: Record<string, any>, conclusion: Record<string, any>): void {
    this.rules.push({ premises, conclusion });
  }
  
  infer(facts: Record<string, any>): Record<string, any> | null {
    for (const rule of this.rules) {
      let match = true;
      for (const [key, value] of Object.entries(rule.premises)) {
        if (facts[key] !== value) {
          match = false;
          break;
        }
      }
      if (match) {
        return rule.conclusion;
      }
    }
    return null;
  }
}
