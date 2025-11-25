import { MotherEquation, ObjectType } from "../core/mother-equation";

export class ConversationalCore extends MotherEquation {
  conversationHistory: Array<{role: string; message: string; timestamp: Date}>;
  context: Record<string, any>;
  
  constructor(name: string) {
    super(ObjectType.ABSTRACT, name);
    this.conversationHistory = [];
    this.context = {};
  }
  
  addMessage(role: string, message: string): void {
    this.conversationHistory.push({
      role,
      message,
      timestamp: new Date()
    });
  }
  
  respond(userMessage: string): string {
    this.addMessage("user", userMessage);
    const response = `Response to: ${userMessage}`;
    this.addMessage("assistant", response);
    return response;
  }
}
