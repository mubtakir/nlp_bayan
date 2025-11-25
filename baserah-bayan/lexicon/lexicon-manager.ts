import { MotherEquation, ObjectType } from "../core/mother-equation";

export class LexiconManager extends MotherEquation {
  words: Map<string, {meaning: string; category: string}>;

  constructor(name: string = "Lexicon") {
    super(ObjectType.LINGUISTIC, name);
    this.words = new Map();
  }

  addWord(word: string, meaning: string, category: string): void {
    this.words.set(word, {meaning, category});
  }

  lookup(word: string): {meaning: string; category: string} | undefined {
    return this.words.get(word);
  }
}
