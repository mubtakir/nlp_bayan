import { ConversationalCore } from "./conversational-core";

export class DialogueManager {
  conversational: ConversationalCore;
  currentTopic: string | null;

  constructor() {
    this.conversational = new ConversationalCore();
    this.currentTopic = null;
  }

  manageTurn(input: string): string {
    return this.conversational.respond(input);
  }
}
