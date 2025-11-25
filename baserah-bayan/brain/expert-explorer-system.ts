import { MotherEquation, ObjectType } from "../core/mother-equation";

export enum ExpertiseLevel {
  NOVICE = 'novice',
  INTERMEDIATE = 'intermediate',
  ADVANCED = 'advanced',
  EXPERT = 'expert',
  MASTER = 'master'
}

export enum ExplorationStrategy {
  RANDOM_SEARCH = 'random_search',
  GUIDED_EXPLORATION = 'guided_exploration',
  PATTERN_BASED = 'pattern_based',
  HYBRID_APPROACH = 'hybrid_approach',
  REVOLUTIONARY_DISCOVERY = 'revolutionary_discovery'
}

export enum DecisionType {
  EXPERT_DECISION = 'expert_decision',
  EXPLORER_DECISION = 'explorer_decision',
  COLLABORATIVE_DECISION = 'collaborative_decision',
  EMERGENCY_DECISION = 'emergency_decision'
}

export class BaserahExpertCore extends MotherEquation {
  domain: string;
  expertiseLevel: ExpertiseLevel;
  
  constructor(name: string, domain: string = "general") {
    super(ObjectType.ABSTRACT, name);
    this.domain = domain;
    this.expertiseLevel = ExpertiseLevel.NOVICE;
  }
  
  makeRevolutionaryExpertDecision(problem: Record<string, any>): any {
    return {
      decisionType: DecisionType.EXPERT_DECISION,
      solution: { type: "expert_solution", data: problem },
      confidence: 0.8,
      reasoning: "Expert decision",
      revolutionaryTheoriesUsed: ["zero_duality"]
    };
  }
}
