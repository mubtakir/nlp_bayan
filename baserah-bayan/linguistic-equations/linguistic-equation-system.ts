import { MotherEquation, ObjectType } from "../core/mother-equation";
import { AdaptiveRevolutionaryEquation } from "../brain/adaptive-equations-core";

export class LinguisticEquationSystem extends MotherEquation {
  equations: AdaptiveRevolutionaryEquation[];

  constructor(name: string = "LinguisticEquations") {
    super(ObjectType.LINGUISTIC, name);
    this.equations = [];
  }

  addEquation(eq: AdaptiveRevolutionaryEquation): void {
    this.equations.push(eq);
  }

  evaluate(input: string): number {
    return 0;
  }
}
