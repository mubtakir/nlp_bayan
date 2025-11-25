export interface Episode {
  id: string;
  content: any;
  timestamp: Date;
}

export class EpisodicMemory {
  episodes: Episode[];

  constructor() {
    this.episodes = [];
  }

  addEpisode(content: any): void {
    this.episodes.push({
      id: Date.now().toString(),
      content,
      timestamp: new Date()
    });
  }
}
