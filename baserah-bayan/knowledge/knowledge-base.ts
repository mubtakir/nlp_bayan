import { MotherEquation, ObjectType } from "../core/mother-equation";

export class KnowledgeBase extends MotherEquation {
  facts: Map<string, any>;
  
  constructor(name: string) {
    super(ObjectType.ABSTRACT, name);
    this.facts = new Map();
  }
  
  addFact(key: string, value: any): void {
    this.facts.set(key, value);
  }
  
  query(key: string): any {
    return this.facts.get(key) || null;
  }
}
