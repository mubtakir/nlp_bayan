/**
 * المعادلات المتكيفة الثورية - Adaptive Revolutionary Equations
 * ═══════════════════════════════════════════════════════════════════════════════
 */

import { MotherEquation, ObjectType } from "../core/mother-equation";

export enum AdaptationType {
  ZERO_DUALITY = "zero_duality",
  PERPENDICULAR_OPPOSITES = "perpendicular_opposites",
  FILAMENT_THEORY = "filament_theory",
  COMBINED_ADAPTATION = "combined_adaptation"
}

export enum AdaptationTrigger {
  PERFORMANCE_THRESHOLD = "performance_threshold",
  ERROR_ACCUMULATION = "error_accumulation",
  PATTERN_DETECTION = "pattern_detection",
  TIME_BASED = "time_based",
  USER_FEEDBACK = "user_feedback"
}

export class AdaptationStep {
  stepId: string;
  timestamp: Date;
  adaptationType: AdaptationType;
  trigger: AdaptationTrigger | null;
  alphaBefore: number[];
  kBefore: number[];
  betaBefore: number[];
  alphaAfter: number[];
  kAfter: number[];
  betaAfter: number[];
  performanceBefore: number;
  performanceAfter: number;
  adaptationStrength: number;
  description: string;
  success: boolean;

  constructor(adaptationType: AdaptationType, trigger: AdaptationTrigger | null) {
    this.stepId = this.generateId();
    this.timestamp = new Date();
    this.adaptationType = adaptationType;
    this.trigger = trigger;
    this.alphaBefore = [];
    this.kBefore = [];
    this.betaBefore = [];
    this.alphaAfter = [];
    this.kAfter = [];
    this.betaAfter = [];
    this.performanceBefore = 0.0;
    this.performanceAfter = 0.0;
    this.adaptationStrength = 0.1;
    this.description = "";
    this.success = false;
  }

  private generateId(): string {
    return "step_" + Date.now() + "_" + Math.floor(Math.random() * 10000);
  }

  getImprovement(): number {
    return this.performanceAfter - this.performanceBefore;
  }

  wasSuccessful(): boolean {
    return this.success && this.getImprovement() > 0;
  }
}

export class AdaptiveRevolutionaryEquation extends MotherEquation {
  alpha: number[];
  k: number[];
  beta: number[];
  adaptationHistory: AdaptationStep[];
  performanceHistory: number[];
  errorAccumulation: number[];
  adaptationEnabled: boolean;
  adaptationThreshold: number;
  maxAdaptationStrength: number;
  learningRate: number;
  totalAdaptations: number;
  successfulAdaptations: number;
  adaptationEfficiency: number;

  constructor(
    name: string,
    id?: string,
    initialAlpha?: number[],
    initialK?: number[],
    initialBeta?: number[]
  ) {
    super(ObjectType.MATHEMATICAL, name, id);
    this.alpha = initialAlpha || [1.0, 0.5, 0.3];
    this.k = initialK || [2.0, 3.0, 4.0];
    this.beta = initialBeta || [0.1, 0.05, 0.02];
    this.adaptationHistory = [];
    this.performanceHistory = [];
    this.errorAccumulation = [];
    this.adaptationEnabled = true;
    this.adaptationThreshold = 0.1;
    this.maxAdaptationStrength = 0.5;
    this.learningRate = 0.01;
    this.totalAdaptations = 0;
    this.successfulAdaptations = 0;
    this.adaptationEfficiency = 0.0;
  }

  computeGeneralShapeEquation(xData: number[]): number[] {
    const result: number[] = new Array(xData.length).fill(0);
    const numTerms = Math.min(this.alpha.length, this.k.length, this.beta.length);

    for (let i = 0; i < numTerms; i++) {
      for (let j = 0; j < xData.length; j++) {
        const sigmoidPart = this.alpha[i] / (1 + Math.exp(-this.k[i] * xData[j]));
        const linearPart = this.beta[i] * xData[j];
        result[j] += sigmoidPart + linearPart;
      }
    }
    return result;
  }

  evaluatePerformance(xData: number[], targetData?: number[]): number {
    try {
      const result = this.computeGeneralShapeEquation(xData);
      let performance = 0.0;

      if (targetData && targetData.length === result.length) {
        let error = 0.0;
        for (let i = 0; i < result.length; i++) {
          error += Math.pow(result[i] - targetData[i], 2);
        }
        error /= result.length;
        performance = 1.0 / (1.0 + error);
      } else {
        const smoothness = this.calculateSmoothness(result);
        const elegance = this.calculateMathematicalElegance();
        performance = (smoothness + elegance) / 2.0;
      }

      this.performanceHistory.push(performance);
      return performance;
    } catch (e) {
      return 0.0;
    }
  }

  private calculateSmoothness(data: number[]): number {
    if (data.length < 2) return 1.0;

    const differences: number[] = [];
    for (let i = 1; i < data.length; i++) {
      differences.push(data[i] - data[i - 1]);
    }

    const mean = differences.reduce((a, b) => a + b, 0) / differences.length;
    const variance = differences.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / differences.length;
    const stdDev = Math.sqrt(variance);
    const smoothness = 1.0 / (1.0 + stdDev);
    return Math.min(smoothness, 1.0);
  }

  private calculateMathematicalElegance(): number {
    const zeroBalance = this.calculateZeroDualityBalance();
    const perpendicularHarmony = this.calculatePerpendicularHarmony();
    const filamentCoherence = this.calculateFilamentCoherence();
    return (zeroBalance + perpendicularHarmony + filamentCoherence) / 3.0;
  }

  private calculateZeroDualityBalance(): number {
    let positiveSum = 0.0;
    let negativeSum = 0.0;

    for (const alpha of this.alpha) {
      if (alpha > 0) {
        positiveSum += Math.abs(alpha);
      } else {
        negativeSum += Math.abs(alpha);
      }
    }

    if (positiveSum + negativeSum === 0) return 1.0;
    const balance = 1.0 - Math.abs(positiveSum - negativeSum) / (positiveSum + negativeSum);
    return Math.max(balance, 0.0);
  }

  private calculatePerpendicularHarmony(): number {
    if (this.k.length < 2) return 1.0;

    let harmonySum = 0.0;
    let count = 0;

    for (let i = 0; i < this.k.length; i++) {
      for (let j = i + 1; j < this.k.length; j++) {
        const dotProduct = this.k[i] * this.k[j];
        const perpendicularity = 1.0 / (1.0 + Math.abs(dotProduct));
        harmonySum += perpendicularity;
        count++;
      }
    }

    return count > 0 ? harmonySum / count : 1.0;
  }

  private calculateFilamentCoherence(): number {
    const coherenceFactors: number[] = [];

    if (this.alpha.length === this.k.length && this.alpha.length > 1) {
      const correlation = this.calculateCorrelation(this.alpha, this.k);
      if (!isNaN(correlation)) {
        coherenceFactors.push(Math.abs(correlation));
      }
    }

    if (this.k.length === this.beta.length && this.k.length > 1) {
      const correlation = this.calculateCorrelation(this.k, this.beta);
      if (!isNaN(correlation)) {
        coherenceFactors.push(Math.abs(correlation));
      }
    }

    return coherenceFactors.length > 0 ?
      coherenceFactors.reduce((a, b) => a + b, 0) / coherenceFactors.length : 0.5;
  }

  private calculateCorrelation(arr1: number[], arr2: number[]): number {
    if (arr1.length !== arr2.length || arr1.length < 2) return 0.0;

    const mean1 = arr1.reduce((a, b) => a + b, 0) / arr1.length;
    const mean2 = arr2.reduce((a, b) => a + b, 0) / arr2.length;

    let numerator = 0.0;
    let denom1 = 0.0;
    let denom2 = 0.0;

    for (let i = 0; i < arr1.length; i++) {
      const diff1 = arr1[i] - mean1;
      const diff2 = arr2[i] - mean2;
      numerator += diff1 * diff2;
      denom1 += diff1 * diff1;
      denom2 += diff2 * diff2;
    }

    const denominator = Math.sqrt(denom1 * denom2);
    return denominator > 0 ? numerator / denominator : 0.0;
  }

  shouldAdapt(currentPerformance: number): { should: boolean; trigger: AdaptationTrigger | null } {
    if (!this.adaptationEnabled) {
      return { should: false, trigger: null };
    }

    if (currentPerformance < this.adaptationThreshold) {
      return { should: true, trigger: AdaptationTrigger.PERFORMANCE_THRESHOLD };
    }

    if (this.errorAccumulation.length > 5) {
      const recentErrors = this.errorAccumulation.slice(-5);
      const avgError = recentErrors.reduce((a, b) => a + b, 0) / recentErrors.length;
      if (avgError > 0.2) {
        return { should: true, trigger: AdaptationTrigger.ERROR_ACCUMULATION };
      }
    }

    if (this.performanceHistory.length > 10) {
      const recentPerformance = this.performanceHistory.slice(-10);
      const mean = recentPerformance.reduce((a, b) => a + b, 0) / recentPerformance.length;
      const variance = recentPerformance.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / recentPerformance.length;
      const stdDev = Math.sqrt(variance);

      if (stdDev < 0.01) {
        return { should: true, trigger: AdaptationTrigger.PATTERN_DETECTION };
      }
    }

    return { should: false, trigger: null };
  }

  adaptZeroDuality(adaptationStrength: number = 0.1): AdaptationStep {
    const step = new AdaptationStep(AdaptationType.ZERO_DUALITY, AdaptationTrigger.PERFORMANCE_THRESHOLD);
    step.alphaBefore = [...this.alpha];
    step.kBefore = [...this.k];
    step.betaBefore = [...this.beta];
    step.adaptationStrength = adaptationStrength;

    try {
      for (let i = 0; i < this.alpha.length; i++) {
        const variation = (Math.random() - 0.5) * 2 * adaptationStrength;
        this.alpha[i] += variation;
        if (i + 1 < this.alpha.length) {
          this.alpha[i + 1] -= variation * 0.5;
        }
      }

      for (let i = 0; i < this.k.length; i++) {
        const variation = (Math.random() - 0.5) * 2 * adaptationStrength * 0.5;
        this.k[i] += variation;
        if (i + 1 < this.k.length) {
          this.k[i + 1] -= variation * 0.3;
        }
      }

      step.alphaAfter = [...this.alpha];
      step.kAfter = [...this.k];
      step.betaAfter = [...this.beta];
      step.success = true;
      step.description = "تكيف ثنائية الصفر";
    } catch (e) {
      step.success = false;
      step.description = "فشل تكيف ثنائية الصفر";
    }

    return step;
  }

  adaptPerpendicularOpposites(adaptationStrength: number = 0.1): AdaptationStep {
    const step = new AdaptationStep(AdaptationType.PERPENDICULAR_OPPOSITES, AdaptationTrigger.PERFORMANCE_THRESHOLD);
    step.alphaBefore = [...this.alpha];
    step.kBefore = [...this.k];
    step.betaBefore = [...this.beta];
    step.adaptationStrength = adaptationStrength;

    try {
      for (let i = 0; i < this.k.length - 1; i += 2) {
        const angle = Math.PI / 2;
        const magnitude = Math.sqrt(this.k[i] * this.k[i] + this.k[i + 1] * this.k[i + 1]);
        this.k[i] = magnitude * Math.cos(angle) * (1 + (Math.random() - 0.5) * adaptationStrength);
        this.k[i + 1] = magnitude * Math.sin(angle) * (1 + (Math.random() - 0.5) * adaptationStrength);
      }

      step.alphaAfter = [...this.alpha];
      step.kAfter = [...this.k];
      step.betaAfter = [...this.beta];
      step.success = true;
      step.description = "تكيف تعامد الأضداد";
    } catch (e) {
      step.success = false;
      step.description = "فشل تكيف تعامد الأضداد";
    }

    return step;
  }

  adaptFilamentTheory(adaptationStrength: number = 0.1): AdaptationStep {
    const step = new AdaptationStep(AdaptationType.FILAMENT_THEORY, AdaptationTrigger.PERFORMANCE_THRESHOLD);
    step.alphaBefore = [...this.alpha];
    step.kBefore = [...this.k];
    step.betaBefore = [...this.beta];
    step.adaptationStrength = adaptationStrength;

    try {
      for (let i = 0; i < Math.min(this.alpha.length, this.k.length); i++) {
        const coherenceFactor = this.alpha[i] / (Math.abs(this.k[i]) + 1e-10);
        const adjustment = (Math.random() - 0.5) * adaptationStrength * coherenceFactor;
        this.alpha[i] += adjustment;
        this.k[i] += adjustment * 0.5;
      }

      for (let i = 0; i < Math.min(this.k.length, this.beta.length); i++) {
        const coherenceFactor = this.k[i] / (Math.abs(this.beta[i]) + 1e-10);
        const adjustment = (Math.random() - 0.5) * adaptationStrength * 0.1 * coherenceFactor;
        this.beta[i] += adjustment;
      }

      step.alphaAfter = [...this.alpha];
      step.kAfter = [...this.k];
      step.betaAfter = [...this.beta];
      step.success = true;
      step.description = "تكيف نظرية الفتائل";
    } catch (e) {
      step.success = false;
      step.description = "فشل تكيف نظرية الفتائل";
    }

    return step;
  }

  adaptCombined(adaptationStrength: number = 0.1): AdaptationStep {
    const step = new AdaptationStep(AdaptationType.COMBINED_ADAPTATION, AdaptationTrigger.PERFORMANCE_THRESHOLD);
    step.alphaBefore = [...this.alpha];
    step.kBefore = [...this.k];
    step.betaBefore = [...this.beta];
    step.adaptationStrength = adaptationStrength;

    try {
      this.adaptZeroDuality(adaptationStrength * 0.4);
      this.adaptPerpendicularOpposites(adaptationStrength * 0.3);
      this.adaptFilamentTheory(adaptationStrength * 0.3);

      step.alphaAfter = [...this.alpha];
      step.kAfter = [...this.k];
      step.betaAfter = [...this.beta];
      step.success = true;
      step.description = "تكيف مدمج";
    } catch (e) {
      step.success = false;
      step.description = "فشل التكيف المدمج";
    }

    return step;
  }

  performAdaptation(adaptationType?: AdaptationType, adaptationStrength?: number): AdaptationStep {
    const strength = adaptationStrength ?? Math.min(
      this.learningRate * (1 + this.adaptationHistory.length * 0.1),
      this.maxAdaptationStrength
    );

    const type = adaptationType ?? AdaptationType.ZERO_DUALITY;
    let step: AdaptationStep;

    switch (type) {
      case AdaptationType.ZERO_DUALITY:
        step = this.adaptZeroDuality(strength);
        break;
      case AdaptationType.PERPENDICULAR_OPPOSITES:
        step = this.adaptPerpendicularOpposites(strength);
        break;
      case AdaptationType.FILAMENT_THEORY:
        step = this.adaptFilamentTheory(strength);
        break;
      default:
        step = this.adaptCombined(strength);
    }

    this.adaptationHistory.push(step);
    this.totalAdaptations++;
    if (step.success) {
      this.successfulAdaptations++;
    }

    this.adaptationEfficiency = this.totalAdaptations > 0 ?
      this.successfulAdaptations / this.totalAdaptations : 0.0;

    return step;
  }

  autoAdapt(xData: number[], targetData?: number[], maxIterations: number = 5): AdaptationStep[] {
    const adaptationSteps: AdaptationStep[] = [];

    for (let iteration = 0; iteration < maxIterations; iteration++) {
      const currentPerformance = this.evaluatePerformance(xData, targetData);
      const adaptCheck = this.shouldAdapt(currentPerformance);

      if (!adaptCheck.should) break;

      const step = this.performAdaptation();
      step.trigger = adaptCheck.trigger;
      step.performanceBefore = currentPerformance;

      const newPerformance = this.evaluatePerformance(xData, targetData);
      step.performanceAfter = newPerformance;

      adaptationSteps.push(step);

      if (newPerformance < currentPerformance) break;
    }

    return adaptationSteps;
  }

  getStats(): object {
    return {
      totalAdaptations: this.totalAdaptations,
      successfulAdaptations: this.successfulAdaptations,
      adaptationEfficiency: this.adaptationEfficiency,
      currentPerformance: this.performanceHistory.length > 0 ?
        this.performanceHistory[this.performanceHistory.length - 1] : 0.0,
      adaptationHistoryLength: this.adaptationHistory.length,
      alpha: this.alpha,
      k: this.k,
      beta: this.beta
    };
  }
}
