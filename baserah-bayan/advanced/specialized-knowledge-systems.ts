import { MotherEquation, ObjectType } from "../core/mother-equation";

export class SpecializedKnowledgeSystem extends MotherEquation {
  domain: string;
  knowledgeBase: Map<string, any>;

  constructor(name: string, domain: string) {
    super(ObjectType.ABSTRACT, name);
    this.domain = domain;
    this.knowledgeBase = new Map();
  }

  addKnowledge(key: string, value: any): void {
    this.knowledgeBase.set(key, value);
  }

  query(key: string): any {
    return this.knowledgeBase.get(key);
  }
}
