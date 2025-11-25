import { MotherEquation, ObjectType } from "../core/mother-equation";

export class SystemIntegration extends MotherEquation {
  modules: Map<string, any>;

  constructor(name: string = "Integration") {
    super(ObjectType.COMPOSITE, name);
    this.modules = new Map();
  }

  registerModule(name: string, module: any): void {
    this.modules.set(name, module);
  }

  getModule(name: string): any {
    return this.modules.get(name);
  }
}
