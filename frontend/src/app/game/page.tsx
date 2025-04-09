import { Button } from "@/components/ui/button"

export default function GamePage() {
  return (
    <div className="min-h-screen bg-slate-100 p-4">
      <div className="container mx-auto h-full">
        <div className="grid grid-cols-12 gap-4 h-full">
          {/* Player Information Panel */}
          <div className="col-span-3 bg-white rounded-lg shadow p-4">
            <h2 className="text-xl font-bold mb-4">Player Info</h2>
            <div className="space-y-4">
              <div className="p-2 bg-slate-50 rounded">Player 1</div>
              <div className="p-2 bg-slate-50 rounded">Player 2</div>
            </div>
          </div>

          {/* Main Game Board */}
          <div className="col-span-6 bg-white rounded-lg shadow p-4">
            <h2 className="text-xl font-bold mb-4">Game Board</h2>
            <div className="aspect-square bg-slate-50 rounded flex items-center justify-center">
              Board will go here
            </div>
          </div>

          {/* Controls and Event Log */}
          <div className="col-span-3 space-y-4">
            {/* Controls */}
            <div className="bg-white rounded-lg shadow p-4">
              <h2 className="text-xl font-bold mb-4">Controls</h2>
              <div className="space-y-2">
                <Button className="w-full">Roll Dice</Button>
                <Button className="w-full" variant="outline">End Turn</Button>
              </div>
            </div>

            {/* Event Log */}
            <div className="bg-white rounded-lg shadow p-4">
              <h2 className="text-xl font-bold mb-4">Event Log</h2>
              <div className="h-48 overflow-y-auto bg-slate-50 rounded p-2">
                <p className="text-sm">Game events will appear here...</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
} 