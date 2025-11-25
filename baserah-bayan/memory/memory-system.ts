import { MotherEquation, ObjectType } from "../core/mother-equation";

export class MemorySystem extends MotherEquation {
  shortTermMemory: Array<Record<string, any>>;
  longTermMemory: Array<Record<string, any>>;
  
  constructor(name: string) {
    super(ObjectType.ABSTRACT, name);
    this.shortTermMemory = [];
    this.longTermMemory = [];
  }
  
  store(key: string, value: any, longTerm: boolean = false): void {
    const entry = { key, value, timestamp: new Date() };
    if (longTerm) {
      this.longTermMemory.push(entry);
    } else {
      this.shortTermMemory.push(entry);
    }
  }
  
  retrieve(key: string): any {
    const short = this.shortTermMemory.find(e => e.key === key);
    if (short) return short.value;
    
    const long = this.longTermMemory.find(e => e.key === key);
    if (long) return long.value;
    
    return null;
  }
}
