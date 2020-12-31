
use_bpm 120

amp_kick = 2
#amp_kick = 0
kick_cnt = 1
live_loop :kick do
  print kick_cnt
  if (kick_cnt%8 == 0)then
    sample :bd_tek, amp: amp_kick, cutoff: 100
    sleep 0.75
    sample :bd_tek, amp: amp_kick, cutoff: 80
    sleep 0.25
  else
    sample :bd_tek, amp: amp_kick, cutoff: 100
    sleep 1
  end
  kick_cnt += 1
end

amp_snare = 4
#amp_snare = 0
live_loop :snare ,sync: :kick do
  sleep 1
  sample :drum_snare_soft ,amp:amp_snare, start: 0, finish: 0.5, rate: 0.4
  sleep 1
end

amp_hh = 0.25
live_loop :hh ,sync: :kick do
  sleep 0.25
  #with_fx :flanger do
  #  with_fx :reverb ,damp:0.5 do
  sample :drum_snare_hard ,amp:amp_hh ,start: 0.1, finish: 0.2
  #  end
  #end
end

amp_sandstorm = 0
#amp_sandstorm = 1
live_loop :sandstorm ,sync: :kick do
  sleep 0.5
  #with_fx :ixi_techno , phase: 1 do
  sample :ambi_sauna, amp:amp_sandstorm ,start: 0.15, finish: 0.175
  #end
  sleep 0.5
end

amp_bass0 = 1
live_loop :bass0 ,sync: :kick do
  use_synth :fm
  use_synth_defaults amp: amp_bass0
  16.times do
    play_pattern_timed [:r,:D3],[0.25,0.5] ,release: 0.5
  end
end
amp_bass1 = 1
live_loop :bass1 ,sync: :kick do
  use_synth :fm
  use_synth_defaults amp: amp_bass1
  sleep 7
  play_pattern_timed [:F3,:G3,:A3,:F3],[0.25] ,release: 0.5
end

amp_synth0 = 0
amp_synth0 = 2
live_loop :synth0 ,sync: :kick do
  use_synth :blade
  use_synth_defaults amp: amp_synth0
  with_fx :pitch_shift, pitch_dis:0.01 do
    sleep 0.5
    play :F3
    sleep 1.5
    play :E3
    sleep 1.5
    play :F3 ,release: 0.25
    sleep 4.5
  end
end

amp_synth1 = 0
amp_synth1 = 1
live_loop :synth01 ,sync: :kick do
  use_synth :supersaw
  use_synth_defaults amp: amp_synth1
  with_transpose 12 do
    sleep 0.5
    play :F3
    sleep 1.5
    play :E3
    sleep 1.5
    play :F3 ,release: 0.25
    sleep 4.5
  end
end

amp_synth2 = 0
#amp_synth2 = 1

live_loop :synth_test ,sync: :kick do
  use_synth :blade
  with_fx :compressor do
    with_fx :reverb, room: 1 do
      with_fx :bitcrusher, bits: 16, sample_rate: 16000 do
        with_fx :distortion, distort: 0.5 do
          with_fx :distortion, distort: 0.3 do
            with_fx :distortion, distort: 0.3 do
              use_synth :saw
              use_synth_defaults amp: amp_synth2
              play_pattern_timed [:A3,:F3,:G3,:D3],[1,0.5,1,1]
              play_pattern_timed [:F3,:D3,:E3,:D3,:C3],[1,1,1,0.5,0.5,0.5]
              play_pattern_timed [:C3,:D3,:A2,:r],[1.5,0.5,1,3.5]
              play_pattern_timed [:r,:D3,:F3,:G3],[0.5]
            end
          end
        end
      end
    end
  end
end

amp_synth3 = 0
#amp_synth3 = 1
live_loop :synth3 ,sync: :kick do
  use_synth :tri
  use_synth_defaults amp: amp_synth3
  with_fx :reverb ,room: 1 do
    sleep 0.5
    play_chord ring(:A3,:Bb3,:D4,:F4) ,sustain: 2 ,release: 1.5
    sleep 1.5
    play :G3 ,release: 1
    sleep 1.5
    play :F3 ,release: 1
    sleep 4.5
  end
end

amp_synth4 = 0
#amp_synth4 = 1
live_loop :synth4 ,sync: :kick do
  use_synth :tri
  use_synth_defaults amp: amp_synth4
  
  sleep 0.5
  play_chord ring(:A3,:Bb3,:D4,:F4) ,sustain: 2 ,release: 2
  sleep 1.5
  play :G3 ,release: 2
  sleep 1.5
  play :F3 ,release: 2
  sleep 4.5
  
end

# beaty noise pad
cd = [(ring(:D3,:F4,:A5)),(chord(:A4, :minor7)),(chord(:Bb4, :major7))
      ].ring

amp_chord1 = 0
#amp_chord1 = 1
live_loop :sea, sync: :kick do
  use_synth :tech_saws
  use_synth_defaults cutoff: rrand(80, 110), release: rrand(1, 4), amp: amp_chord1
  with_fx :distortion, mix: 0.5 do
    with_fx :hpf, cutoff: 70 do
      with_transpose -12 do
        print cd
        play_chord cd.tick, attack: 0.1, release: 4, sustain: 2
        sleep 4
        play_chord cd.tick, attack: 0.1, release: 4, sustain: 2
        sleep 3
        play_chord cd.tick, attack: 0.1, release: 4, sustain: 2
        sleep 9
      end
    end
  end
end

amp_chord2 = 0
#amp_chord2 = 1
live_loop :sea2, sync: :kick do
  use_synth :blade
  use_synth_defaults cutoff: rrand(80, 110), release: rrand(1, 4), amp: amp_chord2
  with_fx :distortion, mix: 0.75 do
    with_fx :hpf, cutoff: 70 do
      with_transpose -24 do
        print cd
        sleep 4
        play_chord cd.tick, attack: 0.1, release: 4, sustain: 2
        sleep 5
        play_chord cd.tick, attack: 0.1, release: 4, sustain: 2
        sleep 3
        play_chord cd.tick, attack: 0.1, release: 4, sustain: 2
        sleep 4
      end
    end
  end
end

