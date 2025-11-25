export class ReinforcementLearning {
  qTable: Map<string, number>;

  constructor() {
    this.qTable = new Map();
  }

  update(state: string, action: string, reward: number): void {
    const key = `${state}_${action}`;
    this.qTable.set(key, reward);
  }
}
