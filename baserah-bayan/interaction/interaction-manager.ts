import { MotherEquation, ObjectType } from "../core/mother-equation";

export class InteractionManager extends MotherEquation {
  interactions: Array<{type: string; data: any; timestamp: Date}>;

  constructor(name: string = "InteractionManager") {
    super(ObjectType.ABSTRACT, name);
    this.interactions = [];
  }

  recordInteraction(type: string, data: any): void {
    this.interactions.push({type, data, timestamp: new Date()});
  }
}
