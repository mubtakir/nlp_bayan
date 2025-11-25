import { RevolutionaryAgent } from "./revolutionary-agent";
import { NLUNLGSystem } from "./nlu-nlg-system";
import { EnhancedAdaptiveLearning } from "./enhanced-adaptive-learning";

export class AdvancedIntegration {
  agent: RevolutionaryAgent;
  nluNlg: NLUNLGSystem;
  learning: EnhancedAdaptiveLearning;

  constructor() {
    this.agent = new RevolutionaryAgent("MainAgent");
    this.nluNlg = new NLUNLGSystem();
    this.learning = new EnhancedAdaptiveLearning();
  }

  process(input: string): string {
    const parsed = this.nluNlg.understand(input);
    const action = this.agent.act(parsed);
    return this.nluNlg.generate(parsed.intent, action);
  }
}
