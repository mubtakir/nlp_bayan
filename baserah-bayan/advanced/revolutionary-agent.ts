import { MotherEquation, ObjectType } from "../core/mother-equation";
import { BaserahIntegratedExpertExplorer } from "../brain/integrated-expert-explorer";
import { AdaptiveRevolutionaryEquation } from "../brain/adaptive-equations-core";

export class RevolutionaryAgent extends MotherEquation {
  expertExplorer: BaserahIntegratedExpertExplorer;
  adaptiveEquation: AdaptiveRevolutionaryEquation;
  goals: string[];
  currentGoal: string | null;

  constructor(name: string) {
    super(ObjectType.COMPOSITE, name);
    this.expertExplorer = new BaserahIntegratedExpertExplorer(`${name}_Brain`, "general");
    this.adaptiveEquation = new AdaptiveRevolutionaryEquation(`${name}_Equation`);
    this.goals = [];
    this.currentGoal = null;
  }

  setGoal(goal: string): void {
    this.goals.push(goal);
    this.currentGoal = goal;
  }

  act(situation: Record<string, any>): any {
    const decision = this.expertExplorer.solve(situation);
    return decision.solution;
  }
}
