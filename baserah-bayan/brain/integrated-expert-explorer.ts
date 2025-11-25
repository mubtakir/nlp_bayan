import { MotherEquation, ObjectType } from "../core/mother-equation";
import { BaserahExpertCore } from "./expert-explorer-system";
import { BaserahExplorerCore } from "./explorer-core";

export class BaserahIntegratedExpertExplorer extends MotherEquation {
  expert: BaserahExpertCore;
  explorer: BaserahExplorerCore;
  
  constructor(name: string, domain: string = "general") {
    super(ObjectType.COMPOSITE, name);
    this.expert = new BaserahExpertCore(`${name}_Expert`, domain);
    this.explorer = new BaserahExplorerCore(`${name}_Explorer`, domain);
  }
  
  solve(problem: Record<string, any>): any {
    const expertDecision = this.expert.makeRevolutionaryExpertDecision(problem);
    const explorationResult = this.explorer.explore(problem);
    
    return {
      decisionType: "collaborative",
      solution: expertDecision.solution || explorationResult.solution,
      confidence: (expertDecision.confidence + explorationResult.confidence) / 2,
      reasoning: "Collaborative decision",
      revolutionaryTheoriesUsed: expertDecision.revolutionaryTheoriesUsed || []
    };
  }
}
