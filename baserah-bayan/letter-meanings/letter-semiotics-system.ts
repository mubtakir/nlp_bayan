import { MotherEquation, ObjectType } from "../core/mother-equation";

export class LetterSemioticsSystem extends MotherEquation {
  letterMeanings: Map<string, string>;

  constructor(name: string = "LetterSemiotics") {
    super(ObjectType.LINGUISTIC, name);
    this.letterMeanings = new Map();
  }

  setMeaning(letter: string, meaning: string): void {
    this.letterMeanings.set(letter, meaning);
  }

  getMeaning(letter: string): string | undefined {
    return this.letterMeanings.get(letter);
  }
}
