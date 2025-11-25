import { BaserahExpertCore } from "../brain/expert-explorer-system";

export class ExpertGuidedInferenceAdvanced {
  expert: BaserahExpertCore;

  constructor() {
    this.expert = new BaserahExpertCore("InferenceExpert", "inference");
  }

  infer(data: any): any {
    return this.expert.makeRevolutionaryExpertDecision({data});
  }
}
