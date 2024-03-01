from data_sampler import WorldSampler


def main():
    world_sampler = WorldSampler(
        schematic_directory='data/schematics/',
        temp_directory='data/temp/',
        chunk_progress_save_interval=10000,
        chunk_mark_radius=2,
        sample_offset=6,
        sample_size=11,
        sample_interested_block_threshold=50,
        sample_progress_save_interval=1000,
        sampling_purge_interval=3,
        num_workers=16
    )
    # world_sampler.clear_directory('data/worlds')
    world_sampler.sample_directory('data/worlds')


if __name__ == '__main__':
    main()
