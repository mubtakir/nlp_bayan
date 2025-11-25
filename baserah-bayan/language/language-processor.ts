import { MotherEquation, ObjectType } from "../core/mother-equation";

export class LanguageProcessor extends MotherEquation {
  constructor(name: string = "LanguageProcessor") {
    super(ObjectType.LINGUISTIC, name);
  }

  tokenize(text: string): string[] {
    return text.split(/\s+/);
  }

  parse(text: string): any {
    return {tokens: this.tokenize(text)};
  }
}
