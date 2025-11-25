export class ContextManager {
  context: Map<string, any>;

  constructor() {
    this.context = new Map();
  }

  set(key: string, value: any): void {
    this.context.set(key, value);
  }

  get(key: string): any {
    return this.context.get(key);
  }
}
