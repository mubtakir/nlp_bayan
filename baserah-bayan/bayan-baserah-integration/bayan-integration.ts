import { MotherEquation, ObjectType } from "../core/mother-equation";

export class BayanIntegration extends MotherEquation {
  constructor(name: string = "BayanIntegration") {
    super(ObjectType.COMPOSITE, name);
  }

  integrate(): boolean {
    return true;
  }
}
