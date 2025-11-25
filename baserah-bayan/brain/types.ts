export interface Decision {
  decisionType: string;
  problem?: Record<string, any>;
  solution?: any;
  confidence: number;
  reasoning?: string;
  timestamp: Date;
  revolutionaryTheoriesUsed?: string[];
}

export interface ExplorationResult {
  success: boolean;
  solution?: any;
  confidence?: number;
  explorationPath?: string[];
  newPatternsFound?: number;
}
